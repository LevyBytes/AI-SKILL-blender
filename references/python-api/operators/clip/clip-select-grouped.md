# bpy.ops.clip.select_grouped

bpy.ops.clip. select_grouped ( * , group = 'ESTIMATED' )

Pick every track in the designated category

Parameters :

group ( Literal [ 'KEYFRAMED' , 'ESTIMATED' , 'TRACKED' , 'LOCKED' , 'DISABLED' , 'COLOR' , 'FAILED' ] ) – Group, Select tracks by group (optional)

- KEYFRAMED
Keyframed Tracks – Select all keyframed tracks.

- ESTIMATED
Estimated Tracks – Select all estimated tracks.

- TRACKED
Tracked Tracks – Select all tracked tracks.

- LOCKED
Locked Tracks – Select all locked tracks.

- DISABLED
Disabled Tracks – Select all disabled tracks.

- COLOR
Tracks with Same Color – Select all tracks with same color as active track.

- FAILED
Failed Tracks – Select all tracks which failed to be reconstructed.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

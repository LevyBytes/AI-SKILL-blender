# bpy.ops.clip.clear_track_path

bpy.ops.clip. clear_track_path ( * , action = 'REMAINED' , clear_active = False )

Delete trajectories following or preceding the current position, or wipe the entire track

Parameters :

- action ( Literal [ 'UPTO' , 'REMAINED' , 'ALL' ] ) – Action, Clear action to execute (optional)

- UPTO
Clear Up To – Clear path up to current frame.

- REMAINED
Clear Remained – Clear path at remaining frames (after current).

- ALL
Clear All – Clear the whole path.

- clear_active ( bool ) – Clear Active, Clear active track only instead of all selected tracks (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

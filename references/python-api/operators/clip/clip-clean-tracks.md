# bpy.ops.clip.clean_tracks

bpy.ops.clip. clean_tracks ( * , frames = 0 , error = 0.0 , action = 'SELECT' )

Purge tracks having substantial errors or insufficient coverage

Parameters :

- frames ( int ) – Tracked Frames, Affect tracks which are tracked less than the specified number of frames (in [0, inf], optional)

- error ( float ) – Reprojection Error, Affect tracks which have a larger reprojection error (in [0, inf], optional)

- action ( Literal [ 'SELECT' , '`DELETE_TRACK`' , '`DELETE_SEGMENTS`' ] ) – Action, Cleanup action to execute (optional)

- SELECT
Select – Select unclean tracks.

- `DELETE_TRACK`
Delete Track – Delete unclean tracks.

- `DELETE_SEGMENTS`
Delete Segments – Delete unclean segments of tracks.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

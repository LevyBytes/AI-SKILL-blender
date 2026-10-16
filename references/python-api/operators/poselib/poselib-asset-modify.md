# bpy.ops.poselib.asset_modify

bpy.ops.poselib. asset_modify ( * , mode = 'ADJUST' ) 

Refresh the chosen pose asset in the library from the presently selected bones. The mode determines what portion of the asset is refreshed

Parameters :

mode ( Literal [ 'ADJUST' , 'REPLACE' , 'ADD' , 'REMOVE' ] ) – Overwrite Mode, Specify which parts of the pose asset are overwritten (optional)

- ADJUST
Adjust – Update existing channels in the pose asset but don't remove or add any channels.

- REPLACE
Replace with Selection – Completely replace all channels in the pose asset with the current selection.

- ADD
Add Selected Bones – Add channels of the selection to the pose asset. Existing channels will be updated.

- REMOVE
Remove Selected Bones – Remove channels of the selection from the pose asset.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

# bpy.ops.sculpt.symmetrize

bpy.ops.sculpt. symmetrize ( * , merge_tolerance = 0.0005 )

Mirror the topology edits to maintain balance

Parameters :

merge_tolerance ( float ) – Merge Distance, Proximity threshold for merging symmetrical points (in [0, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]
bpy.ops.sculpt. symmetrize ( * , merge_tolerance = 0.0005 )
Symmetrizes the topology modifications.
Parameters: merge_tolerance ( float ) – Merge Distance, Distance within which symmetrical vertices are merged (in [0, inf], optional)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).

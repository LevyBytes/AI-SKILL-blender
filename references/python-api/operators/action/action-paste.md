# bpy.ops.action.paste

bpy.ops.action. paste ( * , offset = 'START' , merge = 'MIX' , flipped = False )

Place keyframes from the clipboard onto the active channels beginning at the current timeline position.

Parameters :

- offset (Literal[Keyframe Paste Offset Items]) – Offset, Adjust frame timing for pasted keys (optional)

- merge (Literal[Keyframe Paste Merge Items]) – Type, Strategy for combining inserted and existing keys (optional)

- flipped ( bool ) – Flipped, Paste keyframes from matching bones on the opposite side if available (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

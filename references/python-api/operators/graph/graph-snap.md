# bpy.ops.graph.snap

bpy.ops.graph.snap ( * , type = 'CFRA' )
Align selected keyframes to designated positions in the timeline or value axis

Parameters:
type ( Literal [ 'CFRA' , 'VALUE' , '`NEAREST_FRAME`' , '`NEAREST_SECOND`' , '`NEAREST_MARKER`' , 'HORIZONTAL' ] ) – Type, (optional)
- CFRA: Realign selected keyframes to match the playhead frame
- VALUE: Reposition selected keyframe heights to the cursor Y coordinate
- `NEAREST_FRAME`: Shift keyframes to whole-frame boundaries (corrects subframe timing errors)
- `NEAREST_SECOND`: Realign keyframes to the nearest whole second mark
- `NEAREST_MARKER`: Reposition keyframes at timeline marker locations
- HORIZONTAL: Straighten out curve handles for smoother transitions

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).

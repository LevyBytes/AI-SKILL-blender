# bpy.ops.pose.propagate

bpy.ops.pose. propagate ( * , mode = '`NEXT_KEY`' , end_frame = 250.0 ) 

Push selected aspects of the current pose forward to future keyframes

Parameters :

- mode ( Literal [ '`NEXT_KEY`' , '`LAST_KEY`' , '`BEFORE_FRAME`' , '`BEFORE_END`' , '`SELECTED_KEYS`' , '`SELECTED_MARKERS`' ] ) – Terminate Mode, Method used to determine when to stop propagating pose to keyframes (optional)

- `NEXT_KEY`
To Next Keyframe – Propagate pose to first keyframe following the current frame only.

- `LAST_KEY`
To Last Keyframe – Propagate pose to the last keyframe only (i.e. making action cyclic).

- `BEFORE_FRAME`
Before Frame – Propagate pose to all keyframes between current frame and 'Frame' property.

- `BEFORE_END`
Before Last Keyframe – Propagate pose to all keyframes from current frame until no more are found.

- `SELECTED_KEYS`
On Selected Keyframes – Propagate pose to all selected keyframes.

- `SELECTED_MARKERS`
On Selected Markers – Propagate pose to all keyframes occurring on frames with Scene Markers after the current frame.

- end_frame ( float ) – End Frame, Frame to stop propagating frames to (for 'Before Frame' mode) (in [1.17549e-38, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]
bpy.ops.pose. propagate ( * , mode = '`NEXT_KEY`' , end_frame = 250.0 )
Copies selected aspects of the current pose to subsequent poses already keyframed.
Parameters:
- mode ( Literal [ '`NEXT_KEY`' , '`LAST_KEY`' , '`BEFORE_FRAME`' , '`BEFORE_END`' , '`SELECTED_KEYS`' , '`SELECTED_MARKERS`' ] ) – Terminate Mode, Method used to determine when to stop propagating pose to keyframes (optional)
- `NEXT_KEY` — To Next Keyframe: propagate the pose only to the first keyframe after the current frame.
- `LAST_KEY` — To Last Keyframe: propagate the pose only to the last keyframe (i.e. making the action cyclic).
- `BEFORE_FRAME` — Before Frame: propagate the pose to all keyframes between the current frame and the 'Frame' property.
- `BEFORE_END` — Before Last Keyframe: propagate the pose to all keyframes from the current frame until no more are found.
- `SELECTED_KEYS` — On Selected Keyframes: propagate the pose to all selected keyframes.
- `SELECTED_MARKERS` — On Selected Markers: propagate the pose to all keyframes occurring on frames with Scene Markers after the current frame.
- end_frame ( float ) – End Frame, Frame to stop propagating frames to (for 'Before Frame' mode) (in [1.17549e-38, inf], optional)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).

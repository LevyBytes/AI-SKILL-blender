# bpy.ops.grease_pencil.join_selection

bpy.ops.grease_pencil.join_selection ( * , type = 'JOINSTROKES' )
Generate a fresh stroke from selected points or strokes

Parameters:
type ( Literal [ 'JOINSTROKES' , 'SPLITCOPY' , 'SPLIT' ] ) – Type, Combination strategy for the highlighted selection (optional)
- JOINSTROKES: Unite selected strokes into one continuous path
- SPLITCOPY: Copy selected points into a separate stroke
- SPLIT: Isolate selected points as an independent stroke

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).

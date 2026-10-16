# bpy.ops.grease_pencil.select_all

bpy.ops.grease_pencil.select_all ( * , action = 'TOGGLE' )
Highlight or unhighlight all visible strokes

Parameters:
action ( Literal [ 'TOGGLE' , 'SELECT' , 'DESELECT' , 'INVERT' ] ) – Action, Selection operation to perform (optional)
- TOGGLE: Reverse the selection state of every element
- SELECT: Highlight every element
- DESELECT: Unhighlight every element
- INVERT: Reverse the selection state of every element

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).

# bpy.ops.grease_pencil.select_random

bpy.ops.grease_pencil.select_random ( * , ratio = 0.5 , seed = 0 , action = 'SELECT' )
Highlight random points from the current stroke selection

Parameters:
- ratio ( float ) – Ratio, What fraction of items to highlight randomly (in [0, 1], optional)
- seed ( int ) – Random Seed, Initialization value for the randomizer (in [0, inf], optional)
- action ( Literal [ 'SELECT' , 'DESELECT' ] ) – Action, Selection operation to perform (optional)
- SELECT: Highlight selected elements
- DESELECT: Unhighlight selected elements

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).

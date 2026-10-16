# bpy.ops.curve.select_random

**bpy.ops.curve.select_random**( * , ratio = 0.5 , seed = 0 , action = 'SELECT' )

Select a random subset of control points.

Parameters:
- ratio ( float ) – Ratio, Proportion of items to randomly select (in [0, 1], optional)
- seed ( int ) – Random Seed, Initialization value for the random number generator (in [0, inf], optional)
- action ( Literal [ 'SELECT' , 'DESELECT' ] ) – Action, Selection action to execute (optional)

- SELECT
Select – Select all elements.

- DESELECT
Deselect – Deselect all elements.

Returns: Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).

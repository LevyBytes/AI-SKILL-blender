# bpy.ops.object.select_random

bpy.ops.object. select_random ( * , ratio = 0.5 , seed = 0 , action = 'SELECT' ) 

Highlight or remove highlighting from random visible objects

Parameters :

- ratio ( float ) – Ratio, Fraction of items to modify (in [0, 1], optional)

- seed ( int ) – Random Seed, State for the random number generator (in [0, inf], optional)

- action ( Literal [ 'SELECT' , 'DESELECT' ] ) – Action, Modify highlighting (optional)

- SELECT
Select – Highlight every element.

- DESELECT
Deselect – Remove highlighting from every element.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

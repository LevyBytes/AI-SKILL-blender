# bpy.ops.particle.select_random

bpy.ops.particle. select_random ( * , ratio = 0.5 , seed = 0 , action = 'SELECT' , type = 'HAIR' ) 

Pick an arbitrary set of hair or point positions

Parameters :

- ratio ( float ) – Ratio, Portion of items to select randomly (in [0, 1], optional)

- seed ( int ) – Random Seed, Seed for the random number generator (in [0, inf], optional)

- action ( Literal [ 'SELECT' , 'DESELECT' ] ) – Action, Selection action to execute (optional)

- SELECT
Select – Select all elements.

- DESELECT
Deselect – Deselect all elements.

- type ( Literal [ 'HAIR' , 'POINTS' ] ) – Type, Select either hair or points (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

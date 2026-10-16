# bpy.ops.mesh.select_random

bpy.ops.mesh. select_random ( * , ratio = 0.5 , seed = 0 , action = 'SELECT' ) 

Arbitrarily mark parts

Parameters :

- ratio ( float ) – Ratio, How much of the total to mark in a haphazard manner (in [0, 1], optional)

- seed ( int ) – Random Seed, Seed to feed the randomizer (in [0, inf], optional)

- action ( Literal [ 'SELECT' , 'DESELECT' ] ) – Action, What to do with each element (optional)

- SELECT
Select – Mark each part.

- DESELECT
Deselect – Remove marks from each part.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

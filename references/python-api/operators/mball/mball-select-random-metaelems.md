# bpy.ops.mball.select_random_metaelems

bpy.ops.mball. select_random_metaelems ( * , ratio = 0.5 , seed = 0 , action = 'SELECT' )

Randomly select metaball elements

Parameters :

- ratio ( float ) – Ratio, Fraction of items picked at random (in [0, 1], optional)

- seed ( int ) – Random Seed, Seed feeding the random number generator (in [0, inf], optional)

- action ( Literal [ 'SELECT' , 'DESELECT' ] ) – Action, Which selection action to run (optional)

- SELECT
Select – Select every element.

- DESELECT
Deselect – Deselect every element.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

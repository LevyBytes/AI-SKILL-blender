# bpy.ops.transform.vertex_random

bpy.ops.transform. vertex_random ( * , offset = 0.0 , uniform = 0.0 , normal = 0.0 , seed = 0 , wait_for_input = True ) 

Applies a random jitter to the vertices

Parameters :

- offset ( float ) – Amount, Distance to offset (in [-inf, inf], optional)

- uniform ( float ) – Uniform, Increase for uniform offset distance (in [0, 1], optional)

- normal ( float ) – Normal, Align offset direction to normals (in [0, 1], optional)

- seed ( int ) – Random Seed, Seed for the random number generator (in [0, 10000], optional)

- wait_for_input ( bool ) – Wait for Input, (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

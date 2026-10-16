# bpy.ops.sculpt_curves.select_random

bpy.ops.sculpt_curves. select_random ( * , seed = 0 , partial = False , probability = 0.5 , min = 0.0 , constant_per_curve = True )

Vary the existing selection or establish a new random one

Parameters :

- seed ( int ) – Seed, Randomness origin (in [-inf, inf], optional)

- partial ( bool ) – Partial, Permit control points or curves to be partially selected (optional)

- probability ( float ) – Probability, Likelihood of every control point or curve being included (in [0, 1], optional)

- min ( float ) – Min, Lower threshold for the random selection (in [0, 1], optional)

- constant_per_curve ( bool ) – Constant per Curve, The generated random value applies uniformly to all control points of a curve (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

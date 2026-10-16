# bpy.ops.uv.minimize_stretch

bpy.ops.uv. minimize_stretch ( * , fill_holes = True , blend = 0.0 , iterations = 0 ) 

Eases UV stretching by relaxing the angles

Parameters :

- fill_holes ( bool ) – Fill Holes, Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry (optional)

- blend ( float ) – Blend, Blend factor between stretch minimized and original (in [0, 1], optional)

- iterations ( int ) – Iterations, Number of iterations to run, 0 is unlimited when run interactively (in [0, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

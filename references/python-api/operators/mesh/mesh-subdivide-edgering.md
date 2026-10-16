# bpy.ops.mesh.subdivide_edgering

bpy.ops.mesh. subdivide_edgering ( * , number_cuts = 10 , interpolation = 'PATH' , smoothness = 1.0 , profile_shape_factor = 0.0 , profile_shape = 'SMOOTH' ) 

Slice edges crossing the chosen sequence

Parameters :

- number_cuts ( int ) – Number of Cuts, (in [0, 1000], optional)

- interpolation ( Literal [ 'LINEAR' , 'PATH' , 'SURFACE' ] ) – Interpolation, Which blend technique (optional)

- smoothness ( float ) – Smoothness, How much to smooth (in [0, 1000], optional)

- profile_shape_factor ( float ) – Profile Factor, How much interim fresh edges get narrowed/widened (in [-1000, 1000], optional)

- profile_shape (Literal[Proportional Falloff Curve Only Items]) – Profile Shape, Outline of the profile (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

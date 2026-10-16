# bpy.ops.mesh.bridge_edge_loops

bpy.ops.mesh. bridge_edge_loops ( * , type = 'SINGLE' , use_merge = False , merge_factor = 0.5 , twist_offset = 0 , number_cuts = 0 , interpolation = 'PATH' , smoothness = 1.0 , profile_shape_factor = 0.0 , profile_shape = 'SMOOTH' )

Span faces over two or more picked edge loops

Parameters :

- type ( Literal [ 'SINGLE' , 'CLOSED' , 'PAIRS' ] ) – Connect Loops, Method of bridging multiple loops (optional)

- use_merge ( bool ) – Merge, Merge rather than creating faces (optional)

- merge_factor ( float ) – Merge Factor, (in [0, 1], optional)

- twist_offset ( int ) – Twist, Twist offset for closed loops (in [-1000, 1000], optional)

- number_cuts ( int ) – Number of Cuts, (in [0, 1000], optional)

- interpolation ( Literal [ 'LINEAR' , 'PATH' , 'SURFACE' ] ) – Interpolation, Interpolation method (optional)

- smoothness ( float ) – Smoothness, Smoothness factor (in [0, 1000], optional)

- profile_shape_factor ( float ) – Profile Factor, How much intermediary new edges are shrunk/expanded (in [-1000, 1000], optional)

- profile_shape (Literal[Proportional Falloff Curve Only Items]) – Profile Shape, Shape of the profile (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

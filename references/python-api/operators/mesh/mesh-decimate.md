# bpy.ops.mesh.decimate

bpy.ops.mesh. decimate ( * , ratio = 1.0 , use_vertex_group = False , vertex_group_factor = 1.0 , invert_vertex_group = False , use_symmetry = False , symmetry_axis = 'Y' )

Lower geometry detail by removing edges

Parameters :

- ratio ( float ) – Ratio, (in [0, 1], optional)

- use_vertex_group ( bool ) – Vertex Group, Use active vertex group as an influence (optional)

- vertex_group_factor ( float ) – Weight, Vertex group strength (in [0, 1000], optional)

- invert_vertex_group ( bool ) – Invert, Invert vertex group influence (optional)

- use_symmetry ( bool ) – Symmetry, Maintain symmetry on an axis (optional)

- symmetry_axis (Literal[Axis Xyz Items]) – Axis, Axis of symmetry (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

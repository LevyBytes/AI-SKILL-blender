# bpy.ops.mesh.inset

bpy.ops.mesh. inset ( * , use_boundary = True , use_even_offset = True , use_relative_offset = False , use_edge_rail = False , thickness = 0.0 , depth = 0.0 , use_outset = False , use_select_inset = False , use_individual = False , use_interpolate = True , release_confirm = False )

Recede fresh polygons into picked polygons

Parameters :

- use_boundary ( bool ) – Boundary, Inset face boundaries (optional)

- use_even_offset ( bool ) – Offset Even, Scale the offset to give more even thickness (optional)

- use_relative_offset ( bool ) – Offset Relative, Scale the offset by surrounding geometry (optional)

- use_edge_rail ( bool ) – Edge Rail, Inset the region along existing edges (optional)

- thickness ( float ) – Thickness, (in [0, inf], optional)

- depth ( float ) – Depth, (in [-inf, inf], optional)

- use_outset ( bool ) – Outset, Outset rather than inset (optional)

- use_select_inset ( bool ) – Select Outer, Select the new inset faces (optional)

- use_individual ( bool ) – Individual, Individual face inset (optional)

- use_interpolate ( bool ) – Interpolate, Blend face data across the inset (optional)

- release_confirm ( bool ) – Confirm on Release, (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

# bpy.ops.mesh.rip

bpy.ops.mesh. rip ( * , mirror = False , use_proportional_edit = False , proportional_edit_falloff = 'SMOOTH' , proportional_size = 1.0 , use_proportional_connected = False , use_proportional_projected = False , release_confirm = False , use_accurate = False , use_fill = False )

Sever points or edges from neighboring geometry

Parameters :

- mirror ( bool ) – Mirror Editing, (optional)

- use_proportional_edit ( bool ) – Proportional Editing, (optional)

- proportional_edit_falloff (Literal[Proportional Falloff Items]) – Proportional Falloff, Falloff type for proportional editing mode (optional)

- proportional_size ( float ) – Proportional Size, (in [1e-06, inf], optional)

- use_proportional_connected ( bool ) – Connected, (optional)

- use_proportional_projected ( bool ) – Projected (2D), (optional)

- release_confirm ( bool ) – Confirm on Release, Always confirm operation when releasing button (optional)

- use_accurate ( bool ) – Accurate, Use precise mesh transformation (optional)

- use_fill ( bool ) – Fill, Fill the separated area (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

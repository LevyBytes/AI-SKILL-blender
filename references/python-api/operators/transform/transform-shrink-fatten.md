# bpy.ops.transform.shrink_fatten

bpy.ops.transform. shrink_fatten ( * , value = 0.0 , use_even_offset = False , mirror = False , use_proportional_edit = False , proportional_edit_falloff = 'SMOOTH' , proportional_size = 1.0 , use_proportional_connected = False , use_proportional_projected = False , snap = False , release_confirm = False , use_accurate = False )
Shrinks/fattens the selected vertices along their normals.
Parameters:
- value ( float ) – Offset, (in [-inf, inf], optional)
- use_even_offset ( bool ) – Offset Even, Scale the offset to give more even thickness (optional)
- mirror ( bool ) – Mirror Editing, (optional)
- use_proportional_edit ( bool ) – Proportional Editing, (optional)
- proportional_edit_falloff (Literal[Proportional Falloff Items]) – Proportional Falloff, Falloff type for proportional editing mode (optional)
- proportional_size ( float ) – Proportional Size, (in [1e-06, inf], optional)
- use_proportional_connected ( bool ) – Connected, (optional)
- use_proportional_projected ( bool ) – Projected (2D), (optional)
- snap ( bool ) – Use Snapping Options, (optional)
- release_confirm ( bool ) – Confirm on Release, Always confirm operation when releasing button (optional)
- use_accurate ( bool ) – Accurate, Use accurate transformation (optional)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).

# bpy.ops.graph.shear

bpy.ops.graph.shear ( * , factor = 0.0 , direction = '`FROM_LEFT`' )
Adjust key values in a linear progression, preserving relative spacing by anchoring to one end

Parameters:
- factor ( float ) – Shear Factor, The magnitude to apply for skewing (in [-inf, inf], optional)
- direction ( Literal [ '`FROM_LEFT`' , '`FROM_RIGHT`' ] ) – Direction, Which boundary acts as the fixed anchor point (optional)
- `FROM_LEFT`: Use the left key as the fixed reference
- `FROM_RIGHT`: Use the right key as the fixed reference

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).

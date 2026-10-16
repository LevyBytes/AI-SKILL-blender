# bpy.ops.curve.select_similar

**bpy.ops.curve.select_similar**( * , type = 'WEIGHT' , compare = 'EQUAL' , threshold = 0.1 )

Select curve points that share a similar attribute value.

Parameters:
- type ( Literal [ 'TYPE' , 'RADIUS' , 'WEIGHT' , 'DIRECTION' ] ) – Type, (optional)
- compare ( Literal [ 'EQUAL' , 'GREATER' , 'LESS' ] ) – Compare, (optional)
- threshold ( float ) – Threshold, (in [0, inf], optional)

Returns: Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).

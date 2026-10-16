# bpy.ops.grease_pencil.cyclical_set

bpy.ops.grease_pencil.cyclical_set ( * , type = 'TOGGLE' , subdivide_cyclic_segment = True )
Toggle closed shape by connecting the final point back to the start

Parameters:
- type ( Literal [ 'CLOSE' , 'OPEN' , 'TOGGLE' ] ) – Type, (optional)
- subdivide_cyclic_segment ( bool ) – Match Point Density, Insert intermediate points along the new segment to maintain spacing (optional)

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).

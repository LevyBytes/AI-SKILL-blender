# bpy.ops.grease_pencil.reproject

bpy.ops.grease_pencil.reproject ( * , type = 'VIEW' , keep_original = False , offset = 0.0 )
Flatten strokes onto a target plane as though they were freshly drawn (useful for correcting view changes or repositioning after deformation)

Parameters:
- type ( Literal [ 'FRONT' , 'SIDE' , 'TOP' , 'VIEW' , 'SURFACE' , 'CURSOR' ] ) – Projection Type, (optional)
- FRONT: Map onto the X-Z plane
- SIDE: Map onto the Y-Z plane
- TOP: Map onto the X-Y plane
- VIEW: Map to align with the current camera viewpoint using cursor placement
- SURFACE: Map onto existing scene geometry as if using surface placement
- CURSOR: Map based on 3D cursor orientation
- keep_original ( bool ) – Keep Original, Retain the original strokes and create a repositioned duplicate (optional)
- offset ( float ) – Surface Offset, (in [0, 10], optional)

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).

# bpy.ops.grease_pencil.paste

bpy.ops.grease_pencil.paste ( * , type = 'ACTIVE' , paste_back = False , keep_world_transform = False )
Insert Grease Pencil points or strokes from clipboard to the current layer

Parameters:
- type ( Literal [ 'ACTIVE' , 'LAYER' ] ) – Type, (optional)
- paste_back ( bool ) – Paste on Back, Position pasted strokes behind all existing ones (optional)
- keep_world_transform ( bool ) – Keep World Transform, Maintain the 3D position of clipboard strokes (optional)

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).

# bpy.ops.view3d.view_axis

bpy.ops.view3d. view_axis ( * , type = 'LEFT' , align_active = False , relative = False ) 

Adopts a standard viewpoint configuration

Parameters :

- type ( Literal [ 'LEFT' , 'RIGHT' , 'BOTTOM' , 'TOP' , 'FRONT' , 'BACK' ] ) - View, Standard viewpoint to apply (optional)

- LEFT
Left - Perspective from the left.

- RIGHT
Right - Perspective from the right.

- BOTTOM
Bottom - Perspective from the bottom.

- TOP
Top - Perspective from the top.

- FRONT
Front - Perspective from the front.

- BACK
Back - Perspective from the back.

- align_active ( bool ) - Align Active, Orients to the active object's axes (optional)

- relative ( bool ) - Relative, Adjusts relative to the current position (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

# bpy.ops.asset.screenshot_preview

bpy.ops.asset. screenshot_preview ( * , p1 = (0, 0) , p2 = (0, 0) , force_square = True )

Record a screen image to serve as a preview for the active asset.

Parameters :

- p1 ( Sequence [ int ] ) – Point 1, First point of the screenshot in screenspace (array of 2 items, in [0, inf], optional)

- p2 ( Sequence [ int ] ) – Point 2, Second point of the screenshot in screenspace (array of 2 items, in [0, inf], optional)

- force_square ( bool ) – Force Square, If enabled, the screenshot will have the same height as width (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

# bpy.ops.image.tile_fill

bpy.ops.image. tile_fill ( * , color = (0.0, 0.0, 0.0, 1.0) , generated_type = 'BLANK' , width = 1024 , height = 1024 , float = False , alpha = True )

Fill the current tile with a generated image

Parameters :

- color ( Sequence [ float ] ) – Color, Color used to fill the image (array of 4 items, in [0, inf], optional)

- generated_type (Literal[Image Generated Type Items]) – Generated Type, Fill with a grid useful for checking UV maps (optional)

- width ( int ) – Width, Image width (in [1, inf], optional)

- height ( int ) – Height, Image height (in [1, inf], optional)

- float ( bool ) – 32-bit Float, Make the image use 32-bit floating-point depth (optional)

- alpha ( bool ) – Alpha, Give the new image an alpha channel (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

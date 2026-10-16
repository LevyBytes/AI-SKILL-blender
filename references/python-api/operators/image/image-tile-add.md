# bpy.ops.image.tile_add

bpy.ops.image. tile_add ( * , number = 1002 , count = 1 , label = '' , fill = True , color = (0.0, 0.0, 0.0, 1.0) , generated_type = 'BLANK' , width = 1024 , height = 1024 , float = False , alpha = True )

Adds a tile to the image

Parameters :

- number ( int ) – Number, UDIM number for the tile (in [1001, 2000], optional)

- count ( int ) – Count, How many tiles to add (in [1, inf], optional)

- label ( str ) – Label, Optional label for the tile (optional, never None)

- fill ( bool ) – Fill, Populate the new tile with a generated image (optional)

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

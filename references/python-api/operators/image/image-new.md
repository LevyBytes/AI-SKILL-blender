# bpy.ops.image.new

bpy.ops.image. new ( * , name = 'Untitled' , width = 1024 , height = 1024 , color = (0.0, 0.0, 0.0, 1.0) , alpha = True , generated_type = 'BLANK' , float = False , use_stereo_3d = False , tiled = False )

Create a new image

Parameters :

- name ( str ) – Name, Name of the image data-block (optional, never None)

- width ( int ) – Width, Image width (in [1, inf], optional)

- height ( int ) – Height, Image height (in [1, inf], optional)

- color ( Sequence [ float ] ) – Color, Color used to fill the image (array of 4 items, in [0, inf], optional)

- alpha ( bool ) – Alpha, Give the new image an alpha channel (optional)

- generated_type (Literal[Image Generated Type Items]) – Generated Type, Fill with a grid useful for checking UV maps (optional)

- float ( bool ) – 32-bit Float, Make the image use 32-bit floating-point depth (optional)

- use_stereo_3d ( bool ) – Stereo 3D, Give the image separate left and right views (optional)

- tiled ( bool ) – Tiled, Make a tiled image (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

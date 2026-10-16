# gpu.types.GPUFrameBuffer: methods

bind ( )

Context manager to ensure balanced bind calls, even in the case of an error.
clear ( * , color = None , depth = None , stencil = None )

Load the color, depth, and stencil textures with a chosen value.
Common values: color=(0.0, 0.0, 0.0, 1.0), depth=1.0, stencil=0.

Parameters :

- color ( Sequence [ float ] | None ) – Sequence of 3 or 4 floats representing (r, g, b, a) .

- depth ( float | None ) – depth value.

- stencil ( int | None ) – stencil value.
read_color ( x , y , xsize , ysize , channels , slot , format , * , data = None )

Pull a rectangle of pixels out of the frame buffer.

Parameters :

- x ( int ) – Lower left corner x of a rectangular block of pixels.

- y ( int ) – Lower left corner y of a rectangular block of pixels.

- xsize ( int ) – Width of the pixel rectangle.

- ysize ( int ) – Height of the pixel rectangle.

- channels ( int ) – Number of components to read.

- slot ( int ) – The framebuffer slot to read data from.

- format ( Literal [ 'FLOAT' , 'INT' , 'UINT' , 'UBYTE' , '`UINT_24_8`' , '10_11_11_REV' ] ) – The format that describes the content of a single channel.
`UINT_24_8` is deprecated, use FLOAT instead.

- data (gpu.types.Buffer | None) – Optional Buffer object to fill with the pixels values.

Returns :

The Buffer with the read pixels.

Return type :
read_depth ( x , y , xsize , ysize , * , data = None )

Pull a block of depth pixels out of the frame buffer.

Parameters :

- x ( int ) – Lower left corner x of a rectangular block of pixels.

- y ( int ) – Lower left corner y of a rectangular block of pixels.

- xsize ( int ) – Width of the pixel rectangle.

- ysize ( int ) – Height of the pixel rectangle.

- data (gpu.types.Buffer | None) – Optional Buffer object to fill with the pixels values.

Returns :

The Buffer with the read pixels.

Return type :
viewport_get ( )

Reports the position and size of the current viewport.

Returns :

The viewport as (x, y, width, height) .

Return type :

tuple[int, int, int, int]
viewport_set ( x , y , xsize , ysize )

Assign the viewport for this framebuffer object.
Note: The viewport state is not saved upon framebuffer rebind.

Parameters :

- x ( int ) – Lower left corner x of the viewport rectangle, in pixels.

- y ( int ) – Lower left corner y of the viewport rectangle, in pixels.

- xsize ( int ) – Width of the viewport.

- ysize ( int ) – Height of the viewport.

[Related references](INDEX.md).

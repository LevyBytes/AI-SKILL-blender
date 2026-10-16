# gpu.state: gpu.state. scissor_get ( )

gpu.state. scissor_get ( )

Fetch the scissor region of the active framebuffer.
Note: Only valid between ‘scissor_set’ and a framebuffer rebind.

Returns :

The scissor of the active framebuffer as a tuple
(x, y, xsize, ysize).
x, y: lower left corner of the scissor rectangle, in pixels.
xsize, ysize: width and height of the scissor rectangle.

Return type :

tuple[int, int, int, int]

[Related references](INDEX.md).

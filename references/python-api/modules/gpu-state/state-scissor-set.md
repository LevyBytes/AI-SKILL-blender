# gpu.state: gpu.state. scissor_set ( x , y , xsize , ysize )

gpu.state. scissor_set ( x , y , xsize , ysize )

Sets the scissor region on the active framebuffer.
Note: The scissor state is not saved upon framebuffer rebind.

Parameters :

- x ( int ) – Lower left corner x coordinate, in pixels.

- y ( int ) – Lower left corner y coordinate, in pixels.

- xsize ( int ) – Width of the scissor rectangle.

- ysize ( int ) – Height of the scissor rectangle.

[Related references](INDEX.md).

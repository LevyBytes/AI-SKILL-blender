# freestyle.utils.ContextFunctions: freestyle.utils.ContextFunctions. read_directional_view_map_pixel ( orientation , level , x , y )

freestyle.utils.ContextFunctions. read_directional_view_map_pixel ( orientation , level , x , y ) 

Reads back one pixel out of one of the oriented view map images.

Parameters :

- orientation ( int ) – A number selecting which orientation to inspect.

- level ( int ) – Which pyramid level the pixel should be read from.

- x ( int ) – Horizontal coordinate of the target pixel, measured from an
origin at the lower-left corner.

- y ( int ) – Vertical coordinate of the target pixel, measured from an
origin at the lower-left corner.

Returns :

The floating-point value stored for that pixel.

Return type :

float

[Related references](INDEX.md).

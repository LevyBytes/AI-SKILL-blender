# bpy.types.BlendDataImages: new

new ( name , width , height , * , alpha = False , float_buffer = False , stereo3d = False , is_data = False , tiled = False ) 

Create a new image in the database

Parameters :

- name ( str ) – New name for the data-block (never None)

- width ( int ) – Width of the image (in [1, inf])

- height ( int ) – Height of the image (in [1, inf])

- alpha ( bool ) – Alpha, Use alpha channel (optional)

- float_buffer ( bool ) – Float Buffer, Create an image with floating-point color (optional)

- stereo3d ( bool ) – Stereo 3D, Create left and right views (optional)

- is_data ( bool ) – Is Data, Create image with non-color data color space (optional)

- tiled ( bool ) – Tiled, Create a tiled image (optional)

Returns :

New image data-block

Return type :

Image

[Related references](INDEX.md).

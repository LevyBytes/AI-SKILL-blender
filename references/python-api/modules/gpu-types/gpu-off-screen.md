# gpu.types.GPUOffScreen

class gpu.types. GPUOffScreen ( width , height , * , format = 'RGBA8' )

This object opens up the off screen buffers.

Parameters :

- width ( int ) – Horizontal dimension of the buffer.

- height ( int ) – Vertical dimension of the buffer.

- format ( Literal [ 'RGBA8' , 'RGBA16' , 'RGBA16F' , 'RGBA32F' ] ) – Internal data format inside GPU memory for color attachment texture.
bind ( )

Context manager to ensure balanced bind calls, even in the case of an error.

Returns :

A context manager for the off-screen binding.

Return type :
draw_view3d ( scene , view_layer , view3d , region , view_matrix , projection_matrix , * , do_color_management = False , draw_background = True )

Render the 3d viewport into the offscreen object.

Parameters :

- scene (bpy.types.Scene) – Scene to draw.

- view_layer (bpy.types.ViewLayer) – View layer to draw.

- view3d (bpy.types.SpaceView3D) – 3D View to get the drawing settings from.

- region (bpy.types.Region) – Region of the 3D View (required as temporary draw target).

- view_matrix (mathutils.Matrix) – View Matrix (e.g. camera.matrix_world.inverted() ).

- projection_matrix (mathutils.Matrix) – Projection Matrix (e.g. camera.calc_matrix_camera(...) ).

- do_color_management ( bool ) – Color manage the output.

- draw_background ( bool ) – Draw background.
free ( )

Release the offscreen object.
Its framebuffer, texture, and render objects stop being reachable afterward.
unbind ( * , restore = True )

Release the offscreen object's binding.

Parameters :

restore ( bool ) – Restore the OpenGL state, can only be used when the state has been saved before.
height

Height of the texture.

Type :

int
texture_color

The color texture attached.

Type :
width

Width of the texture.

Type :

int

[Related references](INDEX.md).

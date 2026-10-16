# bpy.ops.image.import_as_mesh_planes: declaration-and-arguments

bpy.ops.image. import_as_mesh_planes ( * , interpolation = 'Linear' , extension = 'CLIP' , use_auto_refresh = True , relative = True , shader = 'PRINCIPLED' , emit_strength = 1.0 , use_transparency = True , render_method = 'DITHERED' , use_backface_culling = False , show_transparent_back = True , overwrite_material = True , filepath = '' , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , files = None , directory = '' , filter_image = True , filter_movie = True , filter_folder = True , force_reload = False , image_sequence = False , offset = True , offset_axis = '+X' , offset_amount = 0.1 , align_axis = '`CAM_AX`' , prev_align_axis = 'NONE' , align_track = False , size_mode = 'ABSOLUTE' , fill_mode = 'FILL' , height = 1.0 , factor = 600.0 )

Build mesh plane(s) from image files, matching each plane to its image's aspect ratio

Parameters :

- interpolation ( Literal [ 'Linear' , 'Closest' , 'Cubic' , 'Smart' ] ) – Interpolation, How the texture is sampled (optional)

- Linear
Linear – Linear sampling between texels.

- Closest
Closest – Take the nearest texel with no blending.

- Cubic
Cubic – Cubic sampling for smoother results.

- Smart
Smart – Bicubic when magnifying, bilinear otherwise (OSL only).

- extension ( Literal [ 'CLIP' , 'EXTEND' , 'REPEAT' ] ) – Extension, Behavior for pixels sampled outside the image's original bounds (optional)

- CLIP
Clip – Limit to the image size and make pixels outside it transparent.

- EXTEND
Extend – Carry on by repeating the image's edge pixels.

- REPEAT
Repeat – Tile the image across both axes.

- use_auto_refresh ( bool ) – Auto Refresh, Re-read the image whenever the frame changes (optional)

- relative ( bool ) – Relative Paths, Store file paths relative to the blend file (optional)

- shader ( Literal [ 'PRINCIPLED' , 'SHADELESS' , 'EMISSION' ] ) – Shader, Which node shader to apply (optional)

- PRINCIPLED
Principled – Use the Principled shader.

- SHADELESS
Shadeless – Visible only to the camera and to reflections.

- EMISSION
Emission – Use an Emission shader.

- emit_strength ( float ) – Emission Strength, How strongly the plane emits light (in [0, inf], optional)

- use_transparency ( bool ) – Use Alpha, Read the alpha channel for transparency (optional)

- render_method ( Literal [ 'DITHERED' , 'BLENDED' ] ) – Render Method, (optional)

- DITHERED
Dithered – Grayscale hashed transparency that works with render passes and ray-tracing; also called deferred rendering..

- BLENDED
Blended – Colored transparency that does not work with render passes or ray-tracing; also called forward rendering..

- use_backface_culling ( bool ) – Backface Culling, Hide the reverse side of faces with backface culling (optional)

- show_transparent_back ( bool ) – Show Backface, Draw several transparent layers (can cause transparency sorting artifacts) (optional)

- overwrite_material ( bool ) – Overwrite Material, Replace any existing material that shares the same name (optional)

[Related references](INDEX.md).

# bpy.ops.image.import_as_mesh_planes: import_as_mesh_planes camera tracking, sizing and result

bpy.ops.image. import_as_mesh_planes ( * , interpolation = 'Linear' , extension = 'CLIP' , use_auto_refresh = True , relative = True , shader = 'PRINCIPLED' , emit_strength = 1.0 , use_transparency = True , render_method = 'DITHERED' , use_backface_culling = False , show_transparent_back = True , overwrite_material = True , filepath = '' , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , files = None , directory = '' , filter_image = True , filter_movie = True , filter_folder = True , force_reload = False , image_sequence = False , offset = True , offset_axis = '+X' , offset_amount = 0.1 , align_axis = '`CAM_AX`' , prev_align_axis = 'NONE' , align_track = False , size_mode = 'ABSOLUTE' , fill_mode = 'FILL' , height = 1.0 , factor = 600.0 )

- align_track ( bool ) – Track Camera, Constrain the planes so they keep facing the camera (optional)

- size_mode ( Literal [ 'ABSOLUTE' , 'CAMERA' , 'DPI' , 'DPBU' ] ) – Size Mode, How the plane size is worked out (optional)

- ABSOLUTE
Absolute – Use an absolute size.

- CAMERA
Scale to Camera Frame – Size to fit or fill the camera frame.

- DPI
Pixels per Inch – Size from pixels per inch.

- DPBU
Pixels per Blender Unit – Size from pixels per Blender Unit.

- fill_mode ( Literal [ 'FILL' , 'FIT' ] ) – Scale, How the plane is sized against the camera frame (optional)

- FILL
Fill – Cover the camera frame, overflowing its edges.

- FIT
Fit – Keep the whole image inside the camera frame.

- height ( float ) – Height, Height of the plane that gets created (in [0.001, inf], optional)

- factor ( float ) – Definition, Pixels per inch or per Blender Unit (in [1, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

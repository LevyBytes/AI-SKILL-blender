# bpy.ops.image.import_as_mesh_planes: import_as_mesh_planes files, transforms and plane offsets

bpy.ops.image. import_as_mesh_planes ( * , interpolation = 'Linear' , extension = 'CLIP' , use_auto_refresh = True , relative = True , shader = 'PRINCIPLED' , emit_strength = 1.0 , use_transparency = True , render_method = 'DITHERED' , use_backface_culling = False , show_transparent_back = True , overwrite_material = True , filepath = '' , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , files = None , directory = '' , filter_image = True , filter_movie = True , filter_folder = True , force_reload = False , image_sequence = False , offset = True , offset_axis = '+X' , offset_amount = 0.1 , align_axis = '`CAM_AX`' , prev_align_axis = 'NONE' , align_track = False , size_mode = 'ABSOLUTE' , fill_mode = 'FILL' , height = 1.0 , factor = 600.0 )

- filepath ( str ) – File Path, Filepath used for importing the file (optional, never None)

- align ( Literal [ 'WORLD' , 'VIEW' , 'CURSOR' ] ) – Align, (optional)

- WORLD
World – Orient the new object to world space.

- VIEW
View – Orient the new object to the current view.

- CURSOR
3D Cursor – Take the new object's orientation from the 3D cursor.

- location (mathutils.Vector) – Location, (array of 3 items, in [-inf, inf], optional)

- rotation (mathutils.Euler) – Rotation, (array of 3 items, in [-inf, inf], optional)

- files ( bpy_prop_collection [ OperatorFileListElement ]) – files, (optional)

- directory ( str ) – directory, (optional, never None)

- filter_image ( bool ) – filter_image, (optional)

- filter_movie ( bool ) – filter_movie, (optional)

- filter_folder ( bool ) – filter_folder, (optional)

- force_reload ( bool ) – Force Reload, Reload the image even if it is already open somewhere else in Blender (optional)

- image_sequence ( bool ) – Detect Image Sequences, Bring numbered image runs in as a single animated sequence rather than separate planes (optional)

- offset ( bool ) – Offset Planes, Space the planes apart; when off, every plane lands at the same spot (optional)

- offset_axis ( Literal [ '+X' , '+Y' , '+Z' , '-X' , '-Y' , '-Z' ] ) – Offset Direction, Which local axis the planes are arranged along (optional)

- +X
+X – Side by Side to the Left.

- +Y
+Y – Side by Side, Downward.

- +Z
+Z – Stacked Above.

- -X
-X – Side by Side to the Right.

- -Y
-Y – Side by Side, Upward.

- -Z
-Z – Stacked Below.

- offset_amount ( float ) – Offset Distance, Spacing placed between neighboring planes (in [-inf, inf], optional)

[Related references](INDEX.md).

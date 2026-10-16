# bpy.ops.image.import_as_mesh_planes: import_as_mesh_planes facing-axis contracts

bpy.ops.image. import_as_mesh_planes ( * , interpolation = 'Linear' , extension = 'CLIP' , use_auto_refresh = True , relative = True , shader = 'PRINCIPLED' , emit_strength = 1.0 , use_transparency = True , render_method = 'DITHERED' , use_backface_culling = False , show_transparent_back = True , overwrite_material = True , filepath = '' , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , files = None , directory = '' , filter_image = True , filter_movie = True , filter_folder = True , force_reload = False , image_sequence = False , offset = True , offset_axis = '+X' , offset_amount = 0.1 , align_axis = '`CAM_AX`' , prev_align_axis = 'NONE' , align_track = False , size_mode = 'ABSOLUTE' , fill_mode = 'FILL' , height = 1.0 , factor = 600.0 )

- align_axis ( Literal [ '+X' , '+Y' , '+Z' , '-X' , '-Y' , '-Z' , 'CAM' , '`CAM_AX`' ] ) – Align, Which way the planes face (optional)

- +X
+X – Facing positive X.

- +Y
+Y – Facing positive Y.

- +Z
+Z – Facing positive Z.

- -X
-X – Facing negative X.

- -Y
-Y – Facing negative Y.

- -Z
-Z – Facing negative Z.

- CAM
Face Camera – Facing camera.

- `CAM_AX`
Camera's Main Axis – Facing the camera's dominant axis.

- prev_align_axis ( Literal [ '+X' , '+Y' , '+Z' , '-X' , '-Y' , '-Z' , 'CAM' , '`CAM_AX`' , 'NONE' ] ) – prev_align_axis, (optional)

- +X
+X – Facing positive X.

- +Y
+Y – Facing positive Y.

- +Z
+Z – Facing positive Z.

- -X
-X – Facing negative X.

- -Y
-Y – Facing negative Y.

- -Z
-Z – Facing negative Z.

- CAM
Face Camera – Facing camera.

- `CAM_AX`
Camera's Main Axis – Facing the camera's dominant axis.

- NONE
Undocumented.

[Related references](INDEX.md).

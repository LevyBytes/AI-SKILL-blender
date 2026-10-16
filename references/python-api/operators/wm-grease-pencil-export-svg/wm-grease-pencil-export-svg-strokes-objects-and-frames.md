# bpy.ops.wm.grease_pencil_export_svg: grease_pencil_export_svg strokes, objects and frames

bpy.ops.wm. grease_pencil_export_svg ( * , filepath = '' , check_existing = True , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = True , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , use_fill = True , selected_object_type = 'ACTIVE' , frame_mode = 'ACTIVE' , stroke_sample = 0.0 , use_uniform_width = False , use_clip_camera = False )

- use_fill ( bool ) - Fill, Exports drawn lines with fill applied (optional)

- selected_object_type ( Literal [ 'ACTIVE' , 'SELECTED' , 'VISIBLE' ] ) - Object, Which items to include in the export (optional)

- ACTIVE
Active - Restricts export to the current item.

- SELECTED
Selected - Restricts export to highlighted items.

- VISIBLE
Visible - Restricts export to all visible items.

- frame_mode ( Literal [ 'ACTIVE' , 'SELECTED' , 'SCENE' ] ) - Frames, Which frames to include in the export (optional)

- ACTIVE
Active - Restricts export to the current frame.

- SELECTED
Selected - Restricts export to highlighted frames.

- SCENE
Scene - Restricts export to all composition frames.

- stroke_sample ( float ) - Sampling, Fidelity of line sampling. Lower numbers mean higher accuracy, and zero disables sampling (in [0, 100], optional)

- use_uniform_width ( bool ) - Uniform Width, Exports drawn lines with consistent thickness (optional)

- use_clip_camera ( bool ) - Clip Camera, Restricts exported geometry to camera bounds during camera view output (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

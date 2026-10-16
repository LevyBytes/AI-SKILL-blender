# bpy.ops.wm.grease_pencil_export_pdf

bpy.ops.wm. grease_pencil_export_pdf ( * , filepath = '' , check_existing = True , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = True , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , use_fill = True , selected_object_type = 'ACTIVE' , frame_mode = 'ACTIVE' , stroke_sample = 0.0 , use_uniform_width = False ) 

Outputs Grease Pencil as a PDF document

Parameters :

- filepath ( str ) - File Path, Destination file path (optional, never None)

- check_existing ( bool ) - Check Existing, Alerts and verifies before overwriting files (optional)

- filter_blender ( bool ) - Filter .blend files, (optional)

- filter_backup ( bool ) - Filter backup .blend files, (optional)

- filter_image ( bool ) - Filter image files, (optional)

- filter_movie ( bool ) - Filter movie files, (optional)

- filter_python ( bool ) - Filter Python files, (optional)

- filter_font ( bool ) - Filter font files, (optional)

- filter_sound ( bool ) - Filter sound files, (optional)

- filter_text ( bool ) - Filter text files, (optional)

- filter_archive ( bool ) - Filter archive files, (optional)

- filter_btx ( bool ) - Filter btx files, (optional)

- filter_alembic ( bool ) - Filter Alembic files, (optional)

- filter_usd ( bool ) - Filter USD files, (optional)

- filter_obj ( bool ) - Filter OBJ files, (optional)

- filter_volume ( bool ) - Filter OpenVDB volume files, (optional)

- filter_folder ( bool ) - Filter folders, (optional)

- filter_blenlib ( bool ) - Filter Blender IDs, (optional)

- filemode ( int ) - File Browser Mode, Browser configuration for loading .blend files, libraries, or specialized formats (in [1, 9], optional)

- display_type ( Literal [ 'DEFAULT' , '`LIST_VERTICAL`' , '`LIST_HORIZONTAL`' , 'THUMBNAIL' ] ) - Display Type, (optional)

- DEFAULT
Default - Chooses display type based on file type.

- `LIST_VERTICAL`
Short List - Displays files in a compact list.

- `LIST_HORIZONTAL`
Long List - Displays files with comprehensive details.

- THUMBNAIL
Thumbnails - Displays files as preview icons.

- sort_method ( str ) - File sorting mode, (optional)
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

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

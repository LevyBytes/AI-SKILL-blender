# bpy.ops.object.empty_image_add: transform and background placement

bpy.ops.object. empty_image_add ( * , filepath = '' , hide_props_region = True , check_existing = False , filter_blender = False , filter_backup = False , filter_image = True , filter_movie = True , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 9 , relative_path = True , show_multiview = False , use_multiview = False , display_type = 'DEFAULT' , sort_method = '' , name = '' , session_uid = 0 , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , scale = (0.0, 0.0, 0.0) , background = False ) 

- location (mathutils.Vector) – Location, Placement point for the newly inserted object (array of 3 items, in [-inf, inf], optional)

- rotation (mathutils.Euler) – Rotation, Orientation to apply when inserting the object (array of 3 items, in [-inf, inf], optional)

- scale (mathutils.Vector) – Scale, Size scaling during insertion (array of 3 items, in [-inf, inf], optional)

- background ( bool ) – Put in Background, Renders the image behind all scene geometry (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

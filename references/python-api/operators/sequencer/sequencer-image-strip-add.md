# bpy.ops.sequencer.image_strip_add

bpy.ops.sequencer.image_strip_add(*, directory='', files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', move_strips=True, frame_start=0, length=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, fit_method='FIT', set_view_transform=True, image_import_type='DETECT', use_sequence_detection=True, use_placeholders=False)

Insert a picture or sequence of pictures into the sequencer.

Parameters:

- directory (str) – Directory, Containing folder of the file (optional, never None)
- files (bpy_prop_collection[OperatorFileListElement]) – Files, (optional)
- check_existing (bool) – Check Existing, Notify user before overwriting (optional)
- filter_blender (bool) – Filter .blend files, (optional)
- filter_backup (bool) – Filter backup .blend files, (optional)
- filter_image (bool) – Filter image files, (optional)
- filter_movie (bool) – Filter movie files, (optional)
- filter_python (bool) – Filter Python files, (optional)
- filter_font (bool) – Filter font files, (optional)
- filter_sound (bool) – Filter sound files, (optional)
- filter_text (bool) – Filter text files, (optional)
- filter_archive (bool) – Filter archive files, (optional)
- filter_btx (bool) – Filter btx files, (optional)
- filter_alembic (bool) – Filter Alembic files, (optional)
- filter_usd (bool) – Filter USD files, (optional)
- filter_obj (bool) – Filter OBJ files, (optional)
- filter_volume (bool) – Filter OpenVDB volume files, (optional)
- filter_folder (bool) – Filter folders, (optional)
- filter_blenlib (bool) – Filter Blender IDs, (optional)
- filemode (int) – File Browser Mode, Setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
- relative_path (bool) – Relative Path, Use path relative to the .blend file (optional)
- show_multiview (bool) – Enable Multi-View, (optional)
- use_multiview (bool) – Use Multi-View, (optional)
- display_type (Literal['DEFAULT', '`LIST_VERTICAL`', '`LIST_HORIZONTAL`', 'THUMBNAIL']) – Display Type, (optional)
  - DEFAULT
    Default – Infer presentation from file types.
  - `LIST_VERTICAL`
    Short List – Compact file list view.
  - `LIST_HORIZONTAL`
    Long List – Comprehensive file list view.
  - THUMBNAIL
    Thumbnails – Picture previews.
- sort_method (Literal['DEFAULT', '`FILE_SORT_ALPHA`', '`FILE_SORT_EXTENSION`', '`FILE_SORT_TIME`', '`FILE_SORT_SIZE`', '`ASSET_CATALOG`']) – File sorting mode, (optional)
  - DEFAULT
    Default – Infer sorting approach from file types.
  - `FILE_SORT_ALPHA`
    Name – Order file list in alphabetical sequence.
  - `FILE_SORT_EXTENSION`
    Extension – Order file list by file kind.
  - `FILE_SORT_TIME`
    Modified Date – Order files by change timestamp.
  - `FILE_SORT_SIZE`
    Size – Order files by storage size.
  - `ASSET_CATALOG`
    Asset Catalog – Order assets so those in the same collection stay together. Within a single collection, assets are ordered alphabetically. The collections are in order of the expanded collection hierarchy..
- move_strips (bool) – Move Strips, Automatically initiate mouse-driven translation of strips after insertion (optional)
- frame_start (int) – Start Frame, Where on the timeline the strip begins (in [-inf, inf], optional)
- length (int) – Length, Duration of the piece in frames, or length of each piece if adding multiple (in [-inf, inf], optional)
- channel (int) – Channel, Sequencer track for placement (in [1, 128], optional)
- replace_sel (bool) – Replace Selection, Clear prior selections once the operation finishes (optional)
- overlap (bool) – Allow Overlap, Permit new strips to overlap without correction (optional)
- overlap_shuffle_override (bool) – Override Overlap Shuffle Behavior, Use overlap mode from tool configuration (optional)
- skip_locked_or_muted_channels (bool) – Skip Locked or Muted Channels, Bypass muted or protected tracks when inserting (optional)
- fit_method (Literal[Strip Scale Method Items]) – Fit Method, How to scale the image within the viewport (optional)
- set_view_transform (bool) – Set View Transform, Apply appropriate color transform based on media profile (optional)
- image_import_type (Literal['DETECT', 'SEQUENCE', 'INDIVIDUAL']) – Import As, How to handle the chosen pictures (optional)
  - DETECT
    Auto Detect – Add images as separate pieces, unless file naming indicates a numbered sequence, in which case combine into a single picture sequence.
  - SEQUENCE
    Image Sequence – Combine all chosen images into a single picture sequence. The sequence of images doesn't need to match Blender's numbering scheme, so placeholders can't be determined.
  - INDIVIDUAL
    Individual Images – Add each chosen image as a separate piece.
- use_sequence_detection (bool) – Detect Sequences, Automatically recognize picture sequences in chosen files (based on file labels) (optional)
- use_placeholders (bool) – Use Placeholders, Generate placeholder images for missing sequence frames (optional)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

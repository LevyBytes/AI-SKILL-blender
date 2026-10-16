# bpy.ops.wm.previews_batch_clear

bpy.ops.wm. previews_batch_clear ( * , files = None , directory = '' , filter_blender = True , filter_folder = True , use_scenes = True , use_collections = True , use_objects = True , use_intern_data = True , use_trusted = False , use_backups = True ) 

Clears thumbnails in selected .blend files

Parameters :

- files ( bpy_prop_collection [ OperatorFileListElement ]) – files, (optional)

- directory ( str ) – directory, (optional, never None)

- filter_blender ( bool ) – filter_blender, (optional)

- filter_folder ( bool ) – filter_folder, (optional)

- use_scenes ( bool ) – Scenes, Erase thumbnails for scenes (optional)

- use_collections ( bool ) – Collections, Erase thumbnails for collections (optional)

- use_objects ( bool ) – Objects, Erase thumbnails for objects (optional)

- use_intern_data ( bool ) – Materials & Textures, Remove 'internal' previews (materials, textures, images, etc.) (optional)

- use_trusted ( bool ) – Trusted Blend Files, Enable Python evaluation for selected files (optional)

- use_backups ( bool ) – Save Backups, Keep a backup (.blend1) version of the files when saving with cleared previews (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/file.py:204

[Related references](INDEX.md).

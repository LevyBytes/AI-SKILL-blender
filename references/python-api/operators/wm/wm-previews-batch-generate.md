# bpy.ops.wm.previews_batch_generate

bpy.ops.wm. previews_batch_generate ( * , files = None , directory = '' , filter_blender = True , filter_folder = True , use_scenes = True , use_collections = True , use_objects = True , use_intern_data = True , use_trusted = False , use_backups = True ) 

Produces thumbnails in selected .blend files

Parameters :

- files ( bpy_prop_collection [ OperatorFileListElement ]) – Collection of file paths with common directory root (optional)

- directory ( str ) – Root path of all files listed in files collection (optional, never None)

- filter_blender ( bool ) – Show Blender files in the File Browser (optional)

- filter_folder ( bool ) – Show folders in the File Browser (optional)

- use_scenes ( bool ) – Scenes, Create thumbnails for scenes (optional)

- use_collections ( bool ) – Collections, Create thumbnails for collections (optional)

- use_objects ( bool ) – Objects, Create thumbnails for objects (optional)

- use_intern_data ( bool ) – Materials & Textures, Create 'internal' previews (materials, textures, images, etc.) (optional)

- use_trusted ( bool ) – Trusted Blend Files, Enable Python evaluation for selected files (optional)

- use_backups ( bool ) – Save Backups, Keep a backup (.blend1) version of the files when saving with generated previews (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/file.py:95

[Related references](INDEX.md).

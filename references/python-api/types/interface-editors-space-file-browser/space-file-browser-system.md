# bpy.types.SpaceFileBrowser: system_bookmarks, system_bookmarks_active, system_folders, system_folders_active

system_bookmarks

The system's bookmarks (default None, readonly)

Type :

bpy_prop_collection[FileBrowserFSMenuEntry]
system_bookmarks_active

Which system bookmark is active (-1 when there is none) (in [-32768, 32767], default 0)

Type :

int
system_folders

The system's folders (typically root, mounted drives, and so on) (default None, readonly)

Type :

bpy_prop_collection[FileBrowserFSMenuEntry]
system_folders_active

Which system folder is active (-1 when there is none) (in [-32768, 32767], default 0)

Type :

int

[Related references](INDEX.md).

# File Paths

## File Paths

The File section of Preferences lets you configure auto-save and set default file paths for blend-files, rendered images, and more. You can set locations for various external files via the options below. Hint: the default path // points at the folder of the currently open blend-file (see Relative Paths).

Data:
Fonts: the default place to browse for text-object font files.
Textures: the default place to browse for image textures.
Sounds: the default place to browse for sound files.
Temporary Files: where temporary save files go; the path must point at an existing directory or it's ignored and the system's temp directory is used, and a blank value likewise falls back to the system's temp directory (see Temporary Directory).
Render:
  Render Output: where rendered images/videos are saved.
  Render Cache: where cached render images are kept.

Asset Libraries — the names and on-drive paths of asset libraries; add one to this list to make Blender aware of it. The name is only for your reference and shows up in asset-library selectors, while the path should point at the library's location. To make a new asset library, set up an empty directory and drop it into the List View — then any asset in any blend-file under it (or its subdirectories) shows up in the Asset Browser.
Import Method: how data is handled when an asset is imported, unless the Asset Browser overrides it.
  Link: the asset is linked into the current blend-file and stays read-only; later edits to the asset file propagate to every file that links it.
  Append — the whole asset and all its dependencies are appended into the current file. Drag a material in three times and you get three independent copies; same for an object. "Dependencies" here means everything the asset relies on — for an object that can be its mesh and materials, but also other objects pulled in by modifiers, constraints, or drivers. Because the file now owns its own copy, later edits to the asset file won't show up in the file it was appended to.
  Append (Reuse Data): this one's specific to the Asset Browser. On an asset's first use it's appended together with its dependencies, exactly as above, but Blender notes where it came from and reuses as much data as possible on later uses. Drag a material in three times and it loads once, then gets assigned three times; drag an object in three times and you get three object copies that all share their mesh data, materials, and so on. Because the file now owns its own copy, later edits to the asset file won't show up here either.
  Pack: brings the asset in as linked data and packs it into the current blend-file straight away, keeping it available even if the original library data changes or goes missing; good for self-contained files that don't lean on external asset-library paths.
Relative Path: use a relative path when linking assets from this library.

Script Directories: extra places to look for Python scripts, each givable a Name to signal its purpose. By default Blender checks several platform-dependent directories for scripts; adding a user script path here brings in one more, handy for keeping your own scripts and add-ons separate from the current Blender version. You'll need to create subfolders matching the structure of the scripts folder in Blender's install directory. These subdirectories are used when present:
startup/: modules here are imported at startup.
addons/: legacy add-ons here are listed in the add-ons preferences.
modules/: modules here can be imported by other scripts.
presets/: presets here are added to the existing presets.
Hint: for add-ons it's now recommended to use a local extension repository if you want extra install/manage locations, defining them as extensions to use them.
Note: restart Blender for any changes to the user scripts to take effect.

Applications:
Image Editor: the path to an external image-editing program.
Animation Player: the program for playing back rendered animations via View Animation; the default, Internal, uses Blender's built-in player, which plays every format Blender supports and needs no third-party app.
Text Editor:
  Program: the command to launch the text editor for Edit Externally, either a full path or a command on $PATH; left blank, the internal editor is used.
  Arguments: the exact format of the arguments the text editor opens files with. The supported expansions: $filepath (the file's absolute path), $line (the line to open at, optional), $column (the column from the line's start, optional), and $line0 & $column0 (as those but zero-based). Example: -f $filepath -l $line -c $column.

Development: shown only with Developer Extras on.
I18n Branches: points at the /branches directory of your local SVN translation copy, so you can translate straight from the UI.

Known Limitations - Permissions on Windows: make sure you have the right privileges to run the executable that accesses the defined path. On Windows, for instance, enabling "Run this program as an administrator" for the executable makes the editor fail to open, due to a limitation in the OS's User Account Control. Running a program with elevated privileges is potentially dangerous.

[Related references](INDEX.md).

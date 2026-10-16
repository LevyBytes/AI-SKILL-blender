# Topbar: External Data, See pack or unpack external data.

External Data
Resources like image textures can live inside the blend-file (packed) or as separate files (unpacked).
Blender tracks all unpacked resources via relative or absolute paths.
See pack or unpack external data.

Automatically Pack Resources
Bundle all active external files and any new files added later. Disable to halt automatic packing of new content; existing packed data remains.

Pack Resources
Collect all active external files into the blend-file. After saving, external files stop being used—changes to them won't appear in the file, and they can be moved or removed.

Unpack Resources
Restore previously packed files as external ones. Decide whether to use existing files or overwrite them.

Pack Linked Libraries
Bundle data-blocks sourced from an external
blend-file into the current one.

Unpack Linked Libraries
Export previously bundled data-blocks back to external blend-files. Overwrites existing files.

Make Paths Relative
Convert all external file paths to be relative to the current blend-file.

Make Paths Absolute
Convert all external file paths to full system paths.

Report Missing Files
Check for broken links to unpacked files. After selecting, a warning appears in the Info editor's header if any are found.

Find Missing Files
Locate and repair broken links. A File Browser opens to let you choose a directory; the search runs recursively across all contained directories.
Every missing file discovered is recovered.
Recovery uses absolute paths; select Make Paths Relative later if needed.

Note

Recovered files may need reloading. Save and reload the entire file to refresh all external resources simultaneously.

Clean Up

Purge Unused Data
Open a dialog to delete unused data-blocks from the blend-file or any Linked Data (cannot be undone).
See the Outliner for more information.

Manage Unused Data
Open an Outliner pop-up in Unused Data mode showing data-blocks and other data that are unused or will be discarded on reload. Includes data-blocks with only a fake user.
Add or remove Fake User by clicking the icon on the right side of the Outliner.

Defaults
This menu controls the startup file used to load default scene, workspace, and interface when creating a new file.

Initially contains the built-in startup scene.
Replace this with your own setup.

Save Startup File
Store the current blend-file as the startup file.

Load Factory Settings
Restore the default startup file and preferences.

When an Application Template is active:

Load Factory Blender Settings
Restore original Blender settings without the current template's changes.

Load Factory (Application Template Name) Settings
Restore original template settings.

See also

Managing Preferences.

Quit Ctrl - Q
Exit Blender. The active scene saves to "quit.blend" in Blender's temp directory
(location shown in "File Paths" tab of the Preferences).

[Related references](INDEX.md).
